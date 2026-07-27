import {Env,json} from '../_lib';
export const onRequestGet:PagesFunction<Env>=async({env})=>json((await env.DB.prepare('SELECT id,started_at,completed_at,imported_by,ordem_filename,nota_filename,status,expected_count,valid_count,error_count,warning_count,closed_count,message FROM import_runs ORDER BY started_at DESC LIMIT 50').all()).results);
