export const DEFAULT_ALERT_RULES={enabled:true,minDays:16,criticalDays:30,minValue:100000,notifyCritical:true,notifyHighValue:true,digestFrequency:'daily'};
export function validateAlertRules(rules){return rules.minDays>=0&&rules.criticalDays>rules.minDays&&rules.minValue>=0&&['daily','weekly','manual'].includes(rules.digestFrequency)}
