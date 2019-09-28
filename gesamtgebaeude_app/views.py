from django.shortcuts import render

# Create your views here.
class GesamtgebaeudeCreateView(LoginRequiredMixin, CreateView):
    model = Gesamtgebaeude
    form_class = flachdaecherForm


    def form_valid(self, form):

        form.instance.user = self.request.user



        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FlachdachCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context
