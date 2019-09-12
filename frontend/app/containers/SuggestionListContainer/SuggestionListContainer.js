import React, { PureComponent } from 'react';
import ReactTable from 'react-table';


export default class SuggestionListContainer extends PureComponent {
    state = {
    };

    static defaultProps = {
        data: [],
    };

    render() {
        return (
        <ReactTable
            data={this.props.data}
            columns={
                [
                    {
                        Header: 'Decision Status',
                        accessor: 'decisionStatus',
                    },
                    {
                        Header: 'Song Name',
                        accessor: 'songName',
                    },
                    {
                        Header: 'Series',
                        accessor: 'songSeries',
                    },
                    {
                        Header: 'Song Link',
                        accessor: 'songLink.link',
                        Cell: row => {
                            if (row.value.startsWith('http')) {
                                return (
                                    <div><a href={row.value}>link</a></div>
                                );
                            }
                            return (
                                <div>
                                    Not a Link
                                </div>
                            )
                        }
                    },
                    {
                        Header: 'Is Youtube',
                        accessor: 'songLink.isYoutubeLink',
                        Cell: row => {
                            if (row.value === true) {
                                return (
                                    <div>Yes</div>
                                );
                            } if (row.value === false) {
                                return (
                                    <div>No</div>
                                );
                            }
                            return (
                                <div>wtf</div>
                            );
                        }
                    },
                ]
            }
        />
        );
    }
}
