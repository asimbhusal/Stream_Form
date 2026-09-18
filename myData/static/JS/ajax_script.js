$(document).ready(function () {

    // Stream Register
    $("#stream_register_btn").click(function (event) {
        event.preventDefault();

        const stream_id = $("#stream_id").val();
        const stream_name = $("#stream_name").val();
        const csrfToken = $("input[name=csrfmiddlewaretoken]").val(); // CSRF token

        console.log("Name: " + stream_name);

        $.ajax({
            url: stream_id ? `/stream/edit/${stream_id}/` : `/stream/add/`,
            method: "POST",

            data: {
                stream_id: stream_id,
                stream_name: stream_name,
                csrfmiddlewaretoken: csrfToken
            },

            success: function (response) {

                $("#stream_name").val("");   // Reset the form fields
                $("#stream_id").val("");

                $("#acknowledge")
                    .text("Stream saved successfully!")
                    .css("color", "green")
                    .fadeIn()
                    .delay(2000)
                    .fadeOut();

                const streamList = $("#stream_list");   // Clear the table
                streamList.empty();

                // Add updated stream list rows
                response.streams.forEach(function (stream) {

                    streamList.append(`
                        <tr>
                            <td>${stream.name}</td>

                            <td>
                                <a href="/stream/edit/${stream.id}/"
                                   class="btn btn-warning btn-sm">
                                    Edit
                                </a>
                            </td>

                            <td>
                                <form action="/stream/delete/${stream.id}/"
                                      method="post"
                                      onsubmit="return confirm('Are you sure you want to delete this stream?');">

                                    <input type="hidden"
                                           name="csrfmiddlewaretoken"
                                           value="${csrfToken}">

                                    <button type="submit"
                                            class="btn btn-danger btn-sm">
                                        Delete
                                    </button>

                                </form>
                            </td>
                        </tr>
                    `);

                });

            },

            error: function (xhr, status, error) {
                console.log(error);
                console.log(xhr.responseText);
            }

        });

    });

});