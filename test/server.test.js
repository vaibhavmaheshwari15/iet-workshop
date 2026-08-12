const { describe, it } = require("node:test");
const assert = require("node:assert/strict");
const request = require("node:http");

const app = require("../src/server");

function requestApp(method, path, body) {
  return new Promise((resolve, reject) => {
    const server = app.listen(0, "127.0.0.1", () => {
      const { port } = server.address();
      const payload = body ? JSON.stringify(body) : undefined;

      const req = request.request(
        {
          hostname: "127.0.0.1",
          port,
          path,
          method,
          headers: body
            ? {
                "Content-Type": "application/json",
                "Content-Length": Buffer.byteLength(payload),
              }
            : undefined,
        },
        (res) => {
          const chunks = [];

          res.on("data", (chunk) => chunks.push(chunk));
          res.on("end", () => {
            server.close();
            const raw = Buffer.concat(chunks).toString("utf8");
            resolve({
              statusCode: res.statusCode,
              body: raw ? JSON.parse(raw) : null,
            });
          });
        },
      );

      req.on("error", (error) => {
        server.close();
        reject(error);
      });

      if (payload) {
        req.write(payload);
      }

      req.end();
    });
  });
}

describe("workshop API", () => {
  it("returns health status", async () => {
    const response = await requestApp("GET", "/health");
    assert.equal(response.statusCode, 200);
    assert.deepEqual(response.body, { status: "ok" });
  });

  it("creates and lists workshop notes", async () => {
    const created = await requestApp("POST", "/api/workshop-notes", {
      content: "Hello from the workshop",
    });

    assert.equal(created.statusCode, 201);
    assert.equal(created.body.content, "Hello from the workshop");

    const listed = await requestApp("GET", "/api/workshop-notes");
    assert.equal(listed.statusCode, 200);
    assert.equal(listed.body.notes.length, 1);
    assert.equal(listed.body.notes[0].content, "Hello from the workshop");
  });
});
