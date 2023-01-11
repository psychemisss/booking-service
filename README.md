# Cyberclub booking manager


<div align="center">
  <kbd>
    <img src="https://i.imgur.com/Othx42n.png" />
  </kbd>
</div>

## Description

Cyber club services booking application.

### Features

- Minimalistic and understandable interface. For booking devices in cyber clubs.
- Batch replication mechanism to prevent loosing data, when remote database/API connection fails.
- S3 automatic backups.
- Service error notifications to Telegram chanel.

### Built with

- Python
- [Streamlit](https://streamlit.io/)
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

## Getting started

### Prerequisites

```
Dependencies are included into docker image, we took care of it. 
```

### Install

```DOCKERFILE
docker pull *herewillbenameofimage*
```

### Configure


* `backups_enabled`: Sets S3 backups state. If set to True, backups will be enabled.
* `s3`
  * `endpoint_url`: S3 endpoint URL
  * `access_key_id`: S3 access key ID
  * `secret_access_key`: S3 secret access key
  * `bucket_name`: bucket name where backups will be stored
  * `backup_interval`: interval between backups
* `telegram_alert_channel_id`: Telegram channel ID where API error alerts will be sent
* `booking_services`: enable or disable services that will be displayed on your booking website
* `booking_services_count`: number of available devices of list of it's names
* `booking_time`: time when booking is available (in hours)
* `booking_interval`: minimal step of time that can be booked (in minutes)
* `min_booking_time`: minimal time to be booked
* `max_booking_time`: maximal time to be booked

### Usage

```DOCKERFILE
docker run -p 8501:8501 *herewillbenameofimage*
```

### Issues

If you got any issues, please, create an issue in this [repository]().

### To-do

- [ ] Telegram integration
- [ ] Dockerizing API and interface
- [ ] Setting up local database deploy (docker-compose)
- [ ] Update interface abstractions to use config.json variables
- [ ] S3 integration
- [ ] Batch replication
- [ ] Remote database/API healthcheck service

### License

This project is licensed under the [License](LICENSE).