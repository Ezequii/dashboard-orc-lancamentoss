import {Env,json} from '../_lib';
export const onRequestGet:PagesFunction<Env>=async({env})=>{const r=await env.DB.prepare('SELECT COUNT(*) n FROM orders').first<any>();return json({count:Number(r?.n||0)});};
