from django.test import TestCase


def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    form = self.get_form()
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)


def form_valid(self, form):
    if self.request == 'POST':
        user = self.request.user
        form = AddFavorite(self.request.post, instance=user)
        if form.is_valid():
            try:
                form.save_m2m()
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка')

    else:
        form = AddFavorite()
    return (self.request, {'form': form})
# Create your tests here.
