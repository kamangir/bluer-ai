title:::

We encourage creating one or more AMIs and launching them through `@instance from_image`. These instances will boot up with `bluer_ai` already installed. Alternatively, the user can launch an instance using `@instance from_template` or through the [aws web interface](https://aws.amazon.com/). Either way, take note of the four digits in the Public DNS (IPv4), then open a terminal and type in,

```bash
@ssh ec2 <ipv4-address>
```

Wait for the machine to boot, then paste the clipboard in the terminal and wait for completion.
