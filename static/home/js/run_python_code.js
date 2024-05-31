function runPythonScript() {
    // Get the path to the Python script.
    var pythonScriptPath = "static/home/py/pose_es.py";
  
    // Run the Python script.
    subprocess.run(["python", static/home/py/pose_es.py]);
  }