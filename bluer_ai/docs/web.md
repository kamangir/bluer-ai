# web

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


![image](../../../assets/web-2026-01-13-12-22-09-pu21uk/17682943725004506077697604217535.jpg?raw=true)

items_receive:::
