import logging
import pytest




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
