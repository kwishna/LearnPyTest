from mock_examples.pg_query import fetch_all_users


def test_fetch_all_users_mocked(mocker):
    # Mock psycopg2.connect to return a mock connection object
    mock_conn = mocker.MagicMock()
    mock_cur = mocker.MagicMock()

    # Configure the cursor to return mock data
    mock_cur.fetchall.return_value = [("Jane Doe", 28), ("John Smith", 30)]

    # Setting up the connection and cursor
    mock_conn.cursor.return_value = mock_cur
    mocker.patch("psycopg2.connect", return_value=mock_conn)

    # Call the function
    result = fetch_all_users()

    # Assertions to verify behavior and results
    assert result == [("Jane Doe", 28), ("John Smith", 30)]
    mock_conn.cursor.assert_called_once()
    mock_cur.execute.assert_called_once_with("SELECT * FROM users")
    mock_cur.fetchall.assert_called_once()
    mock_cur.close.assert_called_once()
    mock_conn.close.assert_called_once()
