"""MCP stdio server for Active-Set QP Solver."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import ActiveSetQP

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "solve_quadratic_program",
                        "description": "Solve convex QP min 1/2 x^T Q x + c^T x via KKT matrix solve",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "Q": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}},
                                "c": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["Q", "c"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "solve_quadratic_program":
            Q = args.get("Q", [])
            c = args.get("c", [])
            sol = ActiveSetQP.solve_unconstrained(Q, c)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"solution": sol}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
