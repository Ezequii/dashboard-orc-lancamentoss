const KEY='amaggiAuditLog';
export function audit(action,details={}){const event={timestamp:new Date().toISOString(),action,details};const log=JSON.parse(localStorage.getItem(KEY)||'[]');localStorage.setItem(KEY,JSON.stringify([...log,event].slice(-200)));return event}
export function getAuditLog(){return JSON.parse(localStorage.getItem(KEY)||'[]')}
export function clearAuditLog(){localStorage.removeItem(KEY)}
