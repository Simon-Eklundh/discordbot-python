from enum import Enum


class Link(str, Enum):
    JDK = 'https://bell-sw.com/pages/downloads/#/java-17-lts'
    Java_Doc = 'https://docs.oracle.com/en/java/javase/17/docs/api/index.html'
    Docker = 'https://hub.docker.com/'
    Docker_Docs = 'https://docs.docker.com/'
    Rust = 'https://www.rust-lang.org/learn/get-started'
    Bot_Source = 'https://github.com/Simon-Eklundh/discordbot-python'
    Bot_source_Java = 'https://github.com/Simon-Eklundh/DiscordBot'
