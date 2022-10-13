<!DOCTYPE html>
<html>
  <head>
    <title>API Request page</title>
  </head>
  <body>
    <h1>API Request page</h1>
    <p>A test calling API</p>
    <!-- call api -->
    <p id="api_response">AQUI VAI ATUALIZAR</p>

    <script>
      //call api and set response to api_response
      fetch("/test")
        .then((response) => response.json())
        .then((data) => {
          document.getElementById("api_response").innerHTML = data[0].hello;
        });
    </script>
  </body>
</html>
