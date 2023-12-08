class BankerAlgorithm:
    def __init__(self, processes, resources, max_demand, allocated):
        self.processes = processes
        self.resources = resources
        self.max_demand = max_demand
        self.allocated = allocated
        self.available = [resources[j] - sum(allocated[i][j] for i in range(len(processes))) for j in range(len(resources))]


    def check_safety(self, process, request):
        # Check if the request is within the maximum demand of the process
        if all(request[i] <= self.max_demand[process][i] - self.allocated[process][i] for i in range(len(self.resources))):
            # Try allocating the resources temporarily
            temp_allocated = [self.allocated[process][j] + request[j] for j in range(len(self.resources))]

            temp_available = [self.available[j] - request[j] for j in range(len(self.resources))]

            # Check if the system remains in a safe state
            if self.safety_check(temp_allocated, temp_available):
                return True
            else:
                return False
        else:
            return False

    def safety_check(self, temp_allocated, temp_available):
        work = temp_available.copy()
        finish = [False] * len(self.processes)

        # Check if a process can finish with the available resources
        while True:
            found = False
            for i in range(len(self.processes)):
                if not finish[i] and all(temp_allocated[i][j] <= work[j] for j in range(len(self.resources))):
                    # If the process can finish, release its resources
                    work = [work[j] + temp_allocated[i][j] for j in range(len(self.resources))]
                    finish[i] = True
                    found = True

            # If no process can finish in this iteration, break the loop
            if not found:
                break

        # If all processes finish, the system is in a safe state
        return all(finish)

    def allocate_resources(self, process, request):
        if self.check_safety(process, request):
            # If the allocation is safe, allocate the resources
            for j in range(len(self.resources)):
                self.allocated[process][j] += request[j]
                self.available[j] -= request[j]
            return True
        else:
            # If the allocation is not safe, reject the request
            return False


# Example Usage:
processes = [0, 1, 2, 3, 4]
resources = [10, 5, 7]
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocated = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

banker = BankerAlgorithm(processes, resources, max_demand, allocated)

# Example: Process 1 requests resources [1, 0, 2]
process_to_request = 1
request_resources = [1, 0, 2]

if banker.allocate_resources(process_to_request, request_resources):
    print(f"Allocation for Process {process_to_request} is safe.")
else:
    print(f"Allocation for Process {process_to_request} is unsafe.")
