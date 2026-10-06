def log_process(func):
    def wrapper(*args, **kwargs):
            print("\n[LOG] Diagnostic process started.")
            result = func(*args, **kwargs)
            print("[LOG] Diagnostic process completed.")
            return result

    return wrapper