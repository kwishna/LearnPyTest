import io
import logging
from collections import defaultdict

import allure
import pytest

log_stream = defaultdict(io.StringIO)


@pytest.fixture(scope="session", autouse=True, name="print_request_info")
def test_show_request_properties(request):
    # print(f"Test Function Name: {request.node.name}")
    # print(f"Test Module Name: {request.node.module.__name__}")
    # print(f"Test File Path: {request.node.fspath}")
    # print(f"Test Directory: {request.node.fspath.dirname}")
    # print(f"Test File Name: {request.node.fspath.basename}")
    # print(f"Test Function: {request.node.originalname}")
    # print(f"Test Class: {request.node.cls}")
    # print(f"Test Function Scope: {request.scope}")
    # print(f"Test Function Keywords: {request.keywords}")
    print(f"{dir(request.node)}")
    """
    The name of the fixture function can later be referenced to cause its invocation ahead of running tests:
    test modules or classes can use the ``pytest.mark.usefixtures(fixturename)`` marker.

    Test functions can directly use fixture names as input arguments in which 
    case the fixture instance returned from the fixture function will be injected.

    Fixtures can provide their values to test functions using ``return`` or ``yield`` statements.
    
    When using ``yield`` the code block after the ``yield`` statement is executed as teardown code regardless of the test
    outcome, and must yield exactly once.

    :param scope:
        The scope for which this fixture is shared; one of ``"function"``
        (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.

        This parameter may also be a callable which receives ``(fixture_name, config)``
        as parameters, and must return a ``str`` with one of the values mentioned above.

        See :ref:`dynamic scope` in the docs for more information.

    :param params:
        An optional list of parameters which will cause multiple invocations
        of the fixture function and all of the tests using it.
        The current parameter is available in ``request.param``.

    :param autouse:
        If True, the fixture func is activated for all tests that can see it.
        If False (the default), an explicit reference is needed to activate
        the fixture.

    :param ids:
        Sequence of ids each corresponding to the params so that they are
        part of the test id. If no ids are provided they will be generated
        automatically from the params.

    :param name:
        The name of the fixture. This defaults to the name of the decorated
        function. If a fixture is used in the same module in which it is
        defined, the function name of the fixture will be shadowed by the
        function arg that requests the fixture; one way to resolve this is to
        name the decorated function ``fixture_<fixturename>`` and then use
        ``@pytest.fixture(name='<fixturename>')``.
    
    ====================================================================================================================
    
    'request' has following attributes
    [
        'addfinalizer', 'applymarker', 'cls', 'config', 'fixturename', 'fixturenames', 'fspath',
        'function', 'getfixturevalue', 'instance', 'keywords', 'module', 'node', 'param_index',
        'path', 'raiseerror', 'scope', 'session'
    ]
    
    // request.config
    [
        'ArgsSource', 'InvocationParams', 'VERBOSITY_ASSERTIONS', 'VERBOSITY_TEST_CASES', '_VERBOSITY_INI_DEFAULT',
        
        '_add_verbosity_ini', '_checkversion', '_cleanup', '_configured', '_consider_importhook', '_decide_args', '_do_configure', '_ensure_unconfigure', '_get_override_ini_value',
        '_get_unknown_ini_keys', '_getconftest_pathlist', '_getini', '_getini_unknown_type', '_inicache', '_inipath', '_initini', '_mark_plugins_for_rewrite', '_opt2dest',
        '_override_ini', '_parser', '_preparse', '_processopt', '_rootpath', '_store', '_tmp_path_factory', '_tmpdirhandler', '_validate_args','_validate_config_options',
        '_validate_plugins', '_verbosity_ini_name', '_warn_about_missing_assertion', '_warn_about_skipped_plugins', '_warn_or_fail_if_strict',
        
        'add_cleanup', 'addinivalue_line', 'args', 'args_source', 'cache', 'cwd_relative_nodeid', 'failures_db', 'fromdictargs', 'get_terminal_writer', 'get_verbosity',
        'getini', 'getoption', 'getvalue', 'getvalueorskip', 'hook', 'inicfg', 'inifile', 'inipath', 'invocation_dir', 'invocation_params', 'issue_config_time_warning',
        'known_args_namespace', 'notify_exception', 'option', 'parse', 'pluginmanager', 'pytest_cmdline_parse', 'pytest_collection', 'pytest_load_initial_conftests',
        'rootdir', 'rootpath', 'stash', 'trace', 'workerinput', 'workeroutput'
    ]
    
    // request.node
    [
        'CollectError', 'Failed', 'Interrupted',
        
        '_abc_impl', '_bestrelpathcache', '_collect_one_node', '_collect_path', '_collection_cache', '_fixturemanager', '_initial_parts', '_initialpaths', '_initialpaths_with_parents',
        '_node_location_to_relpath', '_nodeid', '_notfound', '_repr_failure_py', '_setupstate', '_shouldfail', '_shouldstop', '_store', '_traceback_filter',
        
        'add_marker', 'addfinalizer', 'collect', 'config', 'exitstatus', 'extra_keyword_matches', 'from_config', 'from_parent', 'fspath', 'genitems', 'get_closest_marker',
        'gethookproxy', 'getparent', 'ihook', 'isinitpath', 'items', 'iter_markers', 'iter_markers_with_node', 'iter_parents', 'keywords', 'listchain', 'listextrakeywords',
        'listnames', 'name', 'nodeid', 'own_markers', 'parent', 'path', 'perform_collect', 'pytest_collectreport', 'pytest_collectstart', 'pytest_runtest_logreport',
        'repr_failure', 'session', 'setup', 'shouldfail', 'shouldstop', 'startdir', 'startpath', 'stash', 'teardown', 'testscollected', 'testsfailed', 'trace', 'warn'
    ]
    """
# class MyLogHandler(logging.Handler):
#     def __init__(self):
#         super().__init__()
#         self.setFormatter(
#             logging.Formatter('%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(module)s %(message)s')
#         )
#
#     def emit(self, record):
#         super().emit(record)

def pytest_configure():
    logging.getLogger('test').setLevel(logging.INFO)
    logging.getLogger('mathlib').setLevel(logging.WARNING)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # logger.addHandler(MyLogHandler())

def pytest_addoption(parser):
    parser.addini(
        "implicit_marker",
        "An implicit marker to assign to any test otherwise unmarked"
    )

def pytest_collection_modifyitems(session, config, items):
    implicit_marker = config.getini("implicit_marker")
    if not implicit_marker:
        return

    markers = []
    for line in config.getini("markers"):
        mark, rest = line.split(":", 1)
        if '(' in mark:
            mark, rest = mark.split("(", 1)
        markers.append(mark)

    all_markers = ' or '.join(markers)
    if not all_markers:
        return

    # ALL TESTS RUN CONCURRENTLY.
    for item in items.copy():
        all_markers_names = [item.name for item in list(item.iter_marker_names())]
        item_own_markers = item.own_markers
        flag = False
        for item_args in item_own_markers:
            args = item_args.args
            if True in args or len(args) == 0 or 'skip' in all_markers_names:
                items.remove(item)
                flag = True
                break
            if item_args.name == 'jira':
                for tc in item_args.args:
                    tc_id = tc.replace("_", "-")
                    item.add_markers(allure.testcase(url=f'{tc_id}', name=id))
        if not flag:
            item.add_markers(pytest.mark.asyncio_cooperative)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    print(f"Before running test: {item.name}")
    outcome = yield  # Run the actual test
    report = outcome.get_result()
    print(f"After running test: {item.name}")

    # The code before yield runs before the test.
    # The code after yield runs after the test.
    # outcome.get_result() can be called to get the test result or catch exceptions.


    if report.when == 'teardown':
        if report.failed:
            allure.attach(
                body=f"Test {item.name} failed during teardown.",
                name="Teardown Failure Info",
                attachment_type=allure.attachment_type.TEXT
            )
            # allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

        elif report.passed:
            allure.attach(
                body=f"Test {item.name} passed and teardown completed.",
                name="Teardown Success Info",
                attachment_type=allure.attachment_type.TEXT
            )