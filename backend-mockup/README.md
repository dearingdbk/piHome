Backend response mockups
========================

The backend response mockups consist of a series of static JSON files that
simulate responses from the piHome backend in order to reliably test the
behaviour of frontend components.

To work effectively, the webserver serving these test files must recognize
index.json as a directory index. It may also be helpful to properly serve json
files as `application/json`.