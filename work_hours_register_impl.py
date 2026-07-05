from work_hours_register import WorkHoursRegister


class WorkHoursRegisterImpl(WorkHoursRegister):
    def __init__(self):
        self.workers = {}       # worker_id -> {"position": str, "compensation": int}
        self.total_time = {}    # worker_id -> accumulated finished time in office
        self.in_office = {}     # worker_id -> bool, currently inside the office
        self.enter_time = {}    # worker_id -> timestamp of the current entry

    def add_worker(self, worker_id: str, position: str, compensation: int) -> bool:
        if worker_id in self.workers:
            return False
        self.workers[worker_id] = {"position": position, "compensation": compensation}
        self.total_time[worker_id] = 0
        self.in_office[worker_id] = False
        self.enter_time[worker_id] = 0
        return True

    def register(self, worker_id: str, timestamp: int) -> str:
        if worker_id not in self.workers:
            return "invalid_request"
        if not self.in_office[worker_id]:
            # worker enters the office
            self.in_office[worker_id] = True
            self.enter_time[worker_id] = timestamp
        else:
            # worker leaves the office; close the session
            self.in_office[worker_id] = False
            self.total_time[worker_id] += timestamp - self.enter_time[worker_id]
        return "registered"

    def get(self, worker_id: str):
        if worker_id not in self.workers:
            return None
        return self.total_time[worker_id]
