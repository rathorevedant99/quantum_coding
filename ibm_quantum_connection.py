from qiskit_ibm_runtime import QiskitRuntimeService
 
# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(channel="ibm_quantum", token="302176482768ff93521fde09ccfcdc65f1ae62780ade714582a61c3f5fa85e3b626e412143196a54779048e05cc1d3973d163e78ddaaefcf540e2fe7e7e22758", set_as_default=True)
 
# Load saved credentials
service = QiskitRuntimeService()