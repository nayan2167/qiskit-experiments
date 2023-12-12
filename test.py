from typing import Optional, Sequence, Any
from test.fake_experiment import FakeExperiment, FakeAnalysis
from qiskit_experiments.test.fake_backend import FakeBackend
from qiskit import QuantumCircuit
from qiskit_experiments.framework.base_experiment import BaseExperiment
from qiskit_experiments.framework.base_analysis import BaseAnalysis
from qiskit_experiments.framework.composite import ParallelExperiment, BatchExperiment

class CustomExperiment(BaseExperiment):
    def __init__(self, physical_qubits: Sequence[int], 
                 analysis: BaseAnalysis | None = None, 
                 backend: Any | None = None, 
                 experiment_type: str | None = None):
        super().__init__(physical_qubits, analysis, backend, experiment_type)

    def circuits(self):
        pass

if __name__ == "__main__":
    analysis = FakeAnalysis()
    backend = FakeBackend()
    exp1 = CustomExperiment(physical_qubits=[0],
                            analysis=None,
                            backend=backend,
                            experiment_type="suieee")
    print(exp1.experiment_type)
    exp1.experiment_type = "yeaaa"
    print(exp1.experiment_type)
    

    
    
