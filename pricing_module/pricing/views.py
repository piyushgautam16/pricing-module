# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import PricingConfig
from .forms import PricingConfigForm
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
import logging



class PricingConfigListView(ListView):
    model = PricingConfig
    template_name = 'pricing_config_list.html'
    context_object_name = 'pricing_configs'

class PricingConfigDetailView(DetailView):
    model = PricingConfig
    template_name = 'pricing_config_detail.html'
    context_object_name = 'pricing_config'

class PricingConfigFormView(FormView):
    template_name = 'add_or_edit_pricing_config.html'
    form_class = PricingConfigForm
    success_url = '/pricing/list/'  # Update with your success URL

    def form_valid(self, form):
        form.save()
        # Log who's changing the configuration along with the timestamp
        return super().form_valid(form)

def pricing_config_list(request):
    pricing_configs = PricingConfig.objects.all()
    return render(request, 'pricing/pricing_config_list.html', {'pricing_configs': pricing_configs})

def activate_pricing_config(request, pk):
    pricing_config = get_object_or_404(PricingConfig, pk=pk)
    pricing_config.is_active = True
    pricing_config.save()

    log_message = f"Pricing configuration activated by {request.user.username} at {timezone.now()}: {pricing_config.name} (ID: {pricing_config.id})"
    logger.info(log_message)

    messages.success(request, 'Pricing configuration activated successfully.')
    return redirect('pricing:pricing_config_list')

def deactivate_pricing_config(request, pk):
    pricing_config = get_object_or_404(PricingConfig, pk=pk)
    pricing_config.is_active = False
    pricing_config.save()

    log_message = f"Pricing configuration deactivated by {request.user.username} at {timezone.now()}: {pricing_config.name} (ID: {pricing_config.id})"
    logger.info(log_message)

    messages.success(request, 'Pricing configuration deactivated successfully.')
    return redirect('pricing:pricing_config_list')

def delete_pricing_config(request, pk):
    pricing_config = get_object_or_404(PricingConfig, pk=pk)
    pricing_config_name = pricing_config.name  # Store the name for logging
    
    log_message = f"Pricing configuration deleted by {request.user.username} at {timezone.now()}: {pricing_config.name} (ID: {pricing_config.id})"
    logger.info(log_message)

    pricing_config.delete()
    messages.success(request, f"Pricing configuration {pricing_config_name} deleted successfully.")
    
    return redirect('pricing:pricing_config_list')

def pricing_config_detail(request, pk):
    pricing_config = get_object_or_404(PricingConfig, pk=pk)
    return render(request, 'pricing_config_detail.html', {'pricing_config': pricing_config})

logger = logging.getLogger(__name__)

def add_or_edit_pricing_config(request, pk=None):
    pricing_config = None

    if pk:
        pricing_config = get_object_or_404(PricingConfig, pk=pk)

    if request.method == 'POST':
        form = PricingConfigForm(request.POST, instance=pricing_config)
        if form.is_valid():
            pricing_config = form.save()

            log_message = f"Pricing configuration {'edited' if pk else 'added'} by {request.user.username} at {timezone.now()}: {pricing_config.name} (ID: {pricing_config.id})"
            logger.info(log_message)

            success_message = f"Pricing configuration {'edited' if pk else 'added'} successfully."
            messages.success(request, success_message)

            return redirect('pricing:pricing_config_list')
    else:
        form = PricingConfigForm(instance=pricing_config)

    return render(request, 'pricing/add_or_edit_pricing_config.html', {'form': form, 'pricing_config': pricing_config})


def pricing_form(request):
    return render(request, 'pricing_form.html')
