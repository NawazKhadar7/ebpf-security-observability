"""Run supplemental scenarios with their adjacent metric oracles."""
import argparse
import json
import os
from pathlib import Path
import sys
sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
sys.path.insert(0, str(PROJECT / "src"))

def main(argv=None):
    paths = sorted(HERE.glob("*.case.json"))
    available = {path.name.removesuffix(".case.json"): path for path in paths}
    parser = argparse.ArgumentParser(description="Run supplemental local reference scenarios.")
    parser.add_argument("--case", choices=sorted(available), help="Run one scenario by identifier.")
    parser.add_argument("--list", action="store_true", help="List identifiers without running scenarios.")
    parser.add_argument("--json", action="store_true", help="Print a JSON report including results.")
    args = parser.parse_args(argv)
    if not available:
        parser.error("no supplemental scenarios found")
    if args.list:
        print(json.dumps(sorted(available), indent=2) if args.json else "\n".join(sorted(available)))
        return 0
    from syslab.common import check, validate_case
    from syslab.core import run_case
    selected = [args.case] if args.case else sorted(available)
    reports = []
    for identifier in selected:
        try:
            case = json.loads(available[identifier].read_text(encoding="utf-8"))
            expected = json.loads((HERE / (identifier + ".expected.json")).read_text(encoding="utf-8"))
            validate_case(case)
            if case["id"] != identifier:
                raise ValueError("scenario identifier does not match filename")
            if not expected.get("checks"):
                raise ValueError("scenario oracle has no checks")
            result = run_case(case)
            check(result, expected)
            json.dumps(result, allow_nan=False)
            reports.append({"id": identifier, "passed": True, "result": result})
            if not args.json:
                print("PASS " + identifier)
        except Exception as exc:
            reports.append({"id": identifier, "passed": False, "error": str(exc)})
            if not args.json:
                print("FAIL " + identifier + ": " + str(exc), file=sys.stderr)
    passed = sum(report["passed"] for report in reports)
    if args.json:
        print(json.dumps({"passed": passed, "total": len(reports), "results": reports}, indent=2, allow_nan=False))
    else:
        print(f"{passed}/{len(reports)} supplemental scenarios passed")
    return 0 if passed == len(reports) else 1

if __name__ == "__main__":
    raise SystemExit(main())
