FROM wordpress:6.7-php8.3-apache
# Apache on 3000, like the other apps.
RUN sed -i 's/Listen 80/Listen 3000/' /etc/apache2/ports.conf \
 && sed -i 's/:80>/:3000>/' /etc/apache2/sites-available/000-default.conf
# Copied into the web root by the image's entrypoint along with WordPress.
COPY health.php db.php cpu.php /usr/src/wordpress/
COPY upborne-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/upborne-entrypoint.sh
EXPOSE 3000
ENTRYPOINT ["upborne-entrypoint.sh"]
