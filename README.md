# notification_nagios_whatsapp
Nagios alert notification via WhatsApp, using Twilio with Python script

Para utilizar, crie um conta no https://console.twilio.com/ 

Adicione seus dados (ID e TOKEN) no script

Suba o script para o diretório /usr/local/bin/

Edite o arquivo contacts dentro do diretório /usr/local/etc/nagiosql e deixe assim:
define contact {
        contact_name                    whatsapp
        alias                           Whatsapp
        service_notification_period     24x7
        host_notification_period        24x7
        service_notification_options    c,r
        host_notification_options       d,r
        service_notification_commands   notify-by-whatsapp
        host_notification_commands      host-notify-by-whatsapp
        email                           SEU_EMAIL
        pager                           SEU_WHATSAPP
}

Após isso adicione as duas linhas abaixo, no arquivo commands, no diretório  /usr/local/etc/nagiosql e deixe assim:

define command {
        command_name                    notify-by-whatsapp
        command_line                    /usr/local/bin/nagios-whatsapp.py --object_type service --notificationtype "$NOTIFICATIONTYPE$" --servicestate "$SERVICESTATE$" --hostname "$HOSTNAME$" --servicedesc "$SERVICEDESC$" --output "$SERVICEOUTPUT$" 
        register                        1
}

define command {
        command_name                    host-notify-by-whatsapp
        command_line                    /usr/local/bin/nagios-whatsapp.py --object_type host --notificationtype "$NOTIFICATIONTYPE$" --hoststate "$HOSTSTATE$" --hostname "$HOSTNAME$" --hostaddress "$HOSTADDRESS$" --output "$HOSTOUTPUT$"
        register                        1
}

Após isso, certifique-se se o seu host e service está marcado para enviar notificações para o contato whatsapp.

