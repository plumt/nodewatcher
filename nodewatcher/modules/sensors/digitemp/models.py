from django.utils.translation import ugettext as _

from nodewatcher.core.generator.cgm import models as cgm_models
from nodewatcher.core.registry import registration
from nodewatcher.core.registry.cgm import base as cgm_base

class DigitempPackageConfig(cgm_models.PackageConfig):
    """
    Common configuration for CGM packages.
    """
    # No fields

    class RegistryMeta(cgm_models.PackageConfig.RegistryMeta):
        registry_name = _("Digitemp")

registration.point("node.config").register_item(DigitempPackageConfig)

@cgm_base.register_platform_package("openwrt", "nodewatcher-digitemp", DigitempPackageConfig)
def digitemp_package(node, pkgcfg, cfg):
    """
    Configures the digitemp package for OpenWRT.
    """
    pass