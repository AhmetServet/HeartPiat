# HeartPiat Project

## Description

This project aims to gather various device data and send it to another server (in this case my vps server). \
The project is divided into two parts: \

-   Raspberry Pi: This part is responsible for collecting data from the raspberry and sending it to the server.
-   VPS: This part is responsible for receiving the data and send it via telegram bot.

## Running the project

1. Clone this repository

```bash
git clone
```

### Running on VPS

1. Docker build

```bash
docker build -t heartpiat .
```

2. Docker run

```bash
docker run --restart unless-stopped -d heartpiat
```

### Running on Raspberry Pi

1. Clone this repository

```bash
git clone
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Add the following line to the crontab

```bash
python /path/to/heartpiat/rp5_service/service.py
```
