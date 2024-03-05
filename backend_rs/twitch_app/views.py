import json
from typing import Dict, Any, Optional, List
import pandas as pd
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .constants import outputs_path
from .src.classes.Graph import Graph
from .src.services import get_graph_ids, build_graph_data, calculate_shortest_path


def list_graphs(request: HttpRequest) -> JsonResponse:
    """Django view to list graphs constructed from CSV files."""
    graphs_dir = outputs_path
    graph_ids = get_graph_ids(graphs_dir)

    graphs_data = [build_graph_data(graph_id, graphs_dir) for graph_id in graph_ids]

    return JsonResponse({'graphs': graphs_data})


@csrf_exempt
def shortest_path(request) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data: Dict[str, Any] = json.loads(request.body)
        graph_id: str = data.get("graph_id")
        source_node: int = int(data.get("source_node"))
        destination_node: int = int(data.get("destination_node"))

        # Construct graph from CSV
        edges_path = outputs_path / f'edges_{graph_id}.csv'
        graph = Graph[int]()
        try:
            edges_df = pd.read_csv(edges_path)
            for _, row in edges_df.iterrows():
                graph.add_edge(int(row['numeric_id_1']), int(row['numeric_id_2']))
                graph.add_edge(int(row['numeric_id_2']), int(row['numeric_id_1']))
        except Exception as e:
            return JsonResponse({'error': f'Failed to construct graph: {e}'}, status=500)

        path: Optional[List[int]] = calculate_shortest_path(graph, source_node, destination_node)

        if path is None:
            return JsonResponse({"error": "No path found"})

        return JsonResponse({"status": "success", "path": path})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    except KeyError:
        return JsonResponse({"error": "Missing required parameters"}, status=400)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)
