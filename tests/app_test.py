def test_search_query_not_exist(client):
    """Test the search functionality with a non-existent query string."""
    # Log in as a user (assuming the login function is defined)
    login(client, app.config["USERNAME"], app.config["PASSWORD"])

    # Add a post to the system to ensure the database is not empty
    client.post(
        "/add",
        data=dict(title="Search Test Post", text="This post is searchable"),
        follow_redirects=True,
    )

    # Perform a search query for something that doesn't exist
    response = client.get("/search/?query=nonexistentquery")

    # Decode the response data to make it readable
    print(response.data.decode('utf-8'))

    # Check that the status code is 200 (successful request)
    assert response.status_code == 200

    # Assert that there are no search results by checking for an empty `ul` tag
    assert b'<ul class="entries">\n          \n      </ul>' in response.data

