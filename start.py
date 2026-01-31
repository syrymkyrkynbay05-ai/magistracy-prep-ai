import subprocess
import sys
import os
import time


def run_backend():
    print("🚀 Starting backend server (FastAPI)...")
    backend_dir = os.path.join(os.getcwd(), "backend")
    # Using python from venv if exists, otherwise system python
    venv_python = os.path.join(backend_dir, "venv", "Scripts", "python.exe")
    python_cmd = venv_python if os.path.exists(venv_python) else sys.executable

    return subprocess.Popen(
        [python_cmd, "-m", "uvicorn", "main:app", "--reload", "--port", "8000"],
        cwd=backend_dir,
    )


def run_frontend():
    print("🌐 Starting frontend server (Vite)...")
    # Use shell=True for npm on Windows
    return subprocess.Popen(["npm", "run", "dev"], shell=True)


if __name__ == "__main__":
    try:
        backend_proc = run_backend()
        time.sleep(2)  # Give backend a moment
        frontend_proc = run_frontend()

        print("\n✅ Both servers are running!")
        print("🔗 Frontend: http://localhost:5173")
        print("🔗 Backend API: http://localhost:8000")
        print("\nPress Ctrl+C to stop both servers.")

        # Keep the script running
        while True:
            time.sleep(1)
            if backend_proc.poll() is not None:
                print("Backend process died. Exiting...")
                break
            if frontend_proc.poll() is not None:
                print("Frontend process died. Exiting...")
                break

    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
    finally:
        if "backend_proc" in locals():
            backend_proc.terminate()
        if "frontend_proc" in locals():
            frontend_proc.terminate()
        sys.exit(0)
