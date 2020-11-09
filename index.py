import tornado.web
import tornado.ioloop
import asyncio

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files :
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8882/img/{f.filename}")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path" : "img"})
    ])

    app.listen(8882)
    print("listening on port 8882")

    tornado.ioloop.IOLoop.instance().start()