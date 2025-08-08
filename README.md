# Discord Reminder Bot

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![discord.py](https://img.shields.io/badge/discord.py-2.3.2-7289DA.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple, easy-to-use Discord bot that allows users to set quick reminders. The bot will send you a Direct Message when the time is up, ensuring your reminders are private and timely.

This project is designed for easy setup and deployment, making it perfect for obtaining the Discord Developer Badge or for personal use on your server.

## Features

- **Slash Commands**: Modern and intuitive command interface.
- **Private Notifications**: Reminders are sent via Direct Message (DM) to keep them private.
- **Flexible Time Units**: Set reminders in seconds (s), minutes (m), or hours (h).
- **Lightweight**: Minimal resource usage and no database required.
- **Easy to Deploy**: Ready for deployment on platforms like Railway.

## Commands

The bot has one primary command for all its functionality.

### /reminder

Sets a reminder that will be sent to you via DM after the specified duration.

**Syntax:**
`/reminder time:<duration> message:<your_message>`

**Parameters:**

- `time` (Required): How long to wait before sending the reminder. It must be a number followed by a unit.
  - Valid units: `s` for seconds, `m` for minutes, `h` for hours.
- `message` (Required): The text content of your reminder.

**Examples:**

- To set a reminder for 30 seconds:
  ```sh
  /reminder time:30s message:Check the oven
  ```

- To set a reminder for 15 minutes:
  ```sh
  /reminder time:15m message:Join the weekly team meeting
  ```

- To set a reminder for 15 minutes:
  ```sh
  /reminder time:1h message:Start working on the new feature
  ```

