title:::

```bash
@select
@create_test_asset
@web send
```

http://192.168.43.61:8000/test.json

http://192.168.43.61:8000/test-00.png

---

```bash
@select web-$(@timestamp)
@web receive
@assets publish \
	extensions=jpg,push
```

set:::object_name web-2026-01-13-12-22-09-pu21uk

assets:::get:::object_name/17682943725004506077697604217535.jpg