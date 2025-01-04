from django.utils.translation import gettext_lazy as _


class GenderChoices:
    MALE = "male"
    FEMALE = "female"

    choices = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
    )
