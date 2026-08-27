from redirect_service.redirect_rule_handlers import (
    BrowserRuleHandler,
    HostRuleHandler,
)

rule_config_map = {
    "browser": BrowserRuleHandler,
    "host": HostRuleHandler
}
