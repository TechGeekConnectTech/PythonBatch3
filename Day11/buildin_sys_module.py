import sys

print("Python version", sys.version)
print("Python executable", sys.executable)
print("Python platform", sys.platform)
print("Python path", sys.path)
print("Python modules", list(sys.modules.keys())[:10], "...")  # Print first
sys.exit(0)
print("This line will not be executed.")