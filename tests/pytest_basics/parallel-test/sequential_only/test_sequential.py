from xdist.scheduler.loadscope import LoadScopeScheduling


class MyScheduler(LoadScopeScheduling):
    def _split_scope(self, nodeid):
        if r'tests/parallel-test/sequential_only' in nodeid:
            return 'sequential'
        return nodeid


def pytest_xdist_make_scheduler(config, log):
    return MyScheduler(config, log)