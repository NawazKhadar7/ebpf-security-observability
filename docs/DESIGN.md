# Design

Loading code into a kernel changes networking behavior, so the loader prints a plan by default and only attaches with explicit --apply. It never selects an interface or assumes privileges automatically.
