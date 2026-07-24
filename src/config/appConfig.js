export const APP={name:'Controle de Orçamentos de Serviços',version:'6.0.0',environment:import.meta.env.VITE_APP_ENV||'production',authMode:import.meta.env.VITE_AUTH_MODE||'disabled'};
export const DEFAULT_SETTINGS={slaNormal:7,slaAttention:15,slaHigh:30,tvInterval:45,rankingSize:7,staleHours:24,uniqueRule:'fornecedor+orcamento'};
export const ROLE_PERMISSIONS={visualizador:['view'],operador:['view','export','filter'],administrador:['view','export','filter','governance']};
