#!/usr/bin/env sh
set -eu
if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then echo "Usage: sh load_agent.sh TEST_INTERFACE OBJECT [--apply]" >&2; exit 1; fi
interface="$1"
object="$2"
printf "Planned XDP attach: interface=%s object=%s section=xdp\n" "$interface" "$object"
if [ "${3:-}" = "--apply" ]; then
  ip link set dev "$interface" xdp obj "$object" sec xdp
else
  echo "Dry run only. Pass --apply explicitly to attach on your test machine."
fi
