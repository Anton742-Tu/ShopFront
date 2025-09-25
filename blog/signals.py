from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import BlogPost


@receiver(post_save, sender=BlogPost)
def check_views_and_send_email(sender, instance, **kwargs):
    """
    Отправляет email при достижении 100 просмотров
    """
    # Проверяем, что запись сохранена (не создана) и имеет 100+ просмотров
    if kwargs.get("created", False):
        return  # Пропускаем создание новых записей

    if instance.views_count == 100:
        subject = f'🎉 Поздравление! Запись "{instance.title}" достигла 100 просмотров!'

        message = f"""
        Поздравляем! Ваша запись в блоге достигла значимого рубежа!

        Детали записи:
        - Заголовок: {instance.title}
        - Просмотров: {instance.views_count}
        - Дата создания: {instance.created_at.strftime('%d.%m.%Y %H:%M')}
        - Ссылка: http://127.0.0.1:8000{instance.get_absolute_url()}

        Продолжайте в том же духе! 🚀

        С уважением,
        Команда ShopFront
        """

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            print(f"✅ Email отправлен для записи: {instance.title}")
        except Exception as e:
            print(f"❌ Ошибка отправки email: {e}")
