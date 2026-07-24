import React from'react';import{RefreshCw,WifiOff}from'lucide-react';
export function LoadingState(){return <div className="appState"><RefreshCw className="spin"/><b>Carregando dashboard</b><span>Obtendo a base publicada...</span></div>}
export function ErrorState({message,retry}){return <div className="appState error"><WifiOff/><b>Falha ao carregar os dados</b><span>{message}</span><button onClick={retry}>Tentar novamente</button></div>}
