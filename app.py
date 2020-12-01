from server import (
    App,
    Handler,
    InputResponse,
    PermanentRedirectResponse,
    RedirectResponse,
    StaticHandler,
    TextResponse,
)


class HelloWorldHandler(Handler):
    def get_response(self):
        return TextResponse("Title", "Hello World!")

    def handle(self, url, path):
        response = self.get_response()
        return response


if __name__ == "__main__":
    config = {
        "ip": "localhost",
        "port": 1965,
        "certfile": "cert.pem",
        "keyfile": "key.pem",
        "urls": {
            "": StaticHandler(static_dir="examples/static/", directory_listing=True),
            "/test": StaticHandler(
                static_dir="examples/static/", directory_listing=False
            ),
            "/with-sub": StaticHandler(
                static_dir="examples/static/sub-dir", directory_listing=True
            ),
            "/hello": HelloWorldHandler(),
            # Direct response
            "/direct": TextResponse(title="Direct Response", body="I am here"),
            # Special responses
            # TODO: 10
            "/10": InputResponse(prompt="What's the ultimate answer?"),
            # TODO: 11
            "/30": RedirectResponse(target="/hello"),
            "/31": PermanentRedirectResponse(target="/hello"),
            # TODO: 40 TEMPORARY FAILURE
            # TODO: 41 SERVER UNAVAILABLE
            # TODO: 42 (?) CGI ERROR
            # TODO: 43 (?) PROXY ERROR
            # TODO: 44 SLOW DOWN
            # TODO: 50 PERMANENT FAILURE
            # TODO: 51 NOT FOUND (already covered by other response, but nice to have)
            # TODO: 52 GONE
            # TODO: 53 ? PROXY REQUEST REFUSED
            # TODO: 59 BAD REQUEST
            # TODO: 60 (?) CLIENT CERTIFICATE REQUIRED
            # TODO: 61 (?) CERTIFICATE NOT AUTHORISED
            # TODO: 62 (?) CERTIFICATE NOT VALID
        },
    }
    app = App(**config)
    app.run()