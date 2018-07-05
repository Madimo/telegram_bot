#!/usr/bin/env python3

import config
import pymysql

def main():
    with pymysql.connect(host=config.db_host, user=config.db_user, passwd=config.db_passwd, db=config.db_name) as cursor:
        cursor.execute('''CREATE TABLE `ziroom` (
            `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            `title` text NOT NULL,
            `link` text NOT NULL,
            `createdAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`),
            UNIQUE KEY `id` (`id`)
        )''')

if __name__ == '__main__':
	main()
