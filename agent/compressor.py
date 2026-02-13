def compress_health_data(data):
    sleep = data["sleep"]
    steps = data["steps"]
    
    avg_sleep = sum(sleep) // len(sleep)
    avg_steps = sum(steps) // len(steps)
    
    return {
        "avg_sleep": avg_sleep,
        "avg_steps": avg_steps
    }
