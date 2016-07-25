from django import forms


class ActivityRatingForm(forms.Form):
    RATING_CHOICES = (
        ('0', 'Would not go'),
        ('1', 'Probably would not go'),
        ('2', 'Probably would go'),
        ('3', 'Would go')
    )

    rating = forms.ChoiceField(choices=RATING_CHOICES, required=False, label="", label_suffix='')

    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', "")
        super(ActivityRatingForm, self).__init__(*args, **kwargs)

        if label:
            self.fields['rating'].label = label

    def __str__(self):
        return self.fields['rating'].label
