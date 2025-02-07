To run with custom agent go: (on gpu)
```
>>> cd experiments
>>> python run_RL_agent.py experiment.name=test2 experiment.device="cuda:0" agent=custom agent.debug=True hydra/job_logging=disabled
```



To run with tracking on mlflow:
```
>>> cd experiments
>>> python run_RL_agent.py experiment.name=test2 experiment.device="cuda:0" agent=custom agent.debug=True hydra/job_logging=disabled mlflow.track=True mlflow.tracking_uri="http://127.0.0.1:5000"
```

For what i've run so far, cpu does seem faster so keep that in mind.

```
>>> python run_RL_agent.py experiment.name=test2 experiment.device=cpu agent=custom agent.debug=True hydra/job_logging=disabled

>>> python run_RL_agent.py experiment.name=test2 experiment.device=cpu agent=custom agent.debug=True hydra/job_logging=disabled mlflow.track=True mlflow.tracking_uri="http://127.0.0.1:5000"
```

Running with the custom file:

```
>>> python generate_data.py experiment.name=test3 experiment.device=cpu agent=custom agent.debug=True hydra/job_logging=disabled
```