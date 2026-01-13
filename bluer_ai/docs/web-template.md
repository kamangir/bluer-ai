title:::

# send

```bash
@select
@create_test_asset
@web send
```

http://192.168.43.61:8000/test.json

http://192.168.43.61:8000/test-00.png

items_send:::

# receive

```bash
@select web-$(@timestamp)
@web receive open
@assets publish \
	extensions=jpg,push
```

items_receive:::

set:::object_name web-2026-01-13-12-22-09-pu21uk

assets:::get:::object_name/20260112_212937.jpg