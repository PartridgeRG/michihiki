# Incident 001 — Python Import Error (psutil)

## Summary
- **Date:** 2026-02-12
- **Start:** ~16:10 (local)
- **End:** 16:17 (local)
- **Duration:** ~7 minutes
- **Severity:** Sev-4 (Development inconvenience) 
- **Impacted component:** scripts/process_lister.py
- **Impact:** Script failed to execute because a required dependency was not installed in the active virtual environment.

## Detection
- **How detected:** Manual run of script during Break/Fix drill
- **Error observed:**
```text
Traceback (most recent call last):
  File "/home/nestor/michihiki/scripts/process_lister.py", line 1, in <module>
    import psutil
ModuleNotFoundError: No module named 'psutil'
```

## Timeline (local)
- ~16:10 Uninstalled `psutil` from active virtual environment
- ~16:11 Executed script → observed `ModuleNotFoundError`
- ~16:12 Captured traceback to `/tmp/import_error.txt`
- ~16:13 Reinstalled `psutil`
- ~16:14 Verified successful execution
- ~16:15 Confirmed `psutil` exists in `requirements.txt`
- 16:17 Created incident report

## Root Cause
The `psutil` dependency was already declared in `requirements.txt`, but it was manually removed from the active virtual environment during the drill. Since `process_lister.py` imports `psutil` at runtime, execution failed with `ModuleNotFoundError` when the module was absent.

## Resolution
1. Reinstalled dependency:
   - `python3 -m pip install psutil`
2. Verified script executes successfully.
3. Confirmed `psutil==7.2.2` is pinned in `requirements.txt`.

## Prevention
- After creating or modifying a virtual environment, install dependencies using:
  - `python3 -m pip install -r requirements.txt`
- Avoid manually altering dependencies without syncing the environment.
- If dependency issues occur, recreate the virtual environment from `requirements.txt`.
